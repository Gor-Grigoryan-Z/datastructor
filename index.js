
const { MultiFormatReader, BarcodeFormat, DecodeHintType } = require('@zxing/library');
const { ImageBitmapLuminanceSource, BinaryBitmap, HybridBinarizer } = require('@zxing/library');
const Jimp = require('jimp');
const Tesseract = require('tesseract.js');
const fs = require('fs');
const path = require('path');

async function scanBarcode(imagePath) {
    try 
    {
        const image = await Jimp.read(imagePath);
        const luminanceSource = new ImageBitmapLuminanceSource(await image.getBufferAsync(Jimp.MIME_PNG));
        const binaryBitmap = new BinaryBitmap(new HybridBinarizer(luminanceSource));

        const reader = new MultiFormatReader();
        reader.setHints(new Map([[DecodeHintType.POSSIBLE_FORMATS, [BarcodeFormat.CODE_128, BarcodeFormat.EAN_13]]]));

        const result = reader.decode(binaryBitmap);
        console.log(`Barcode detected:`, result.getText());
        return result.getText();
    } catch (err) {
        console.warn(`No barcode found or error scanning barcode. Trying OCR...`);
        return scanText(imagePath);
    }
}

async function scanText(imagePath) {
    try {
        const { data: { text } } = await Tesseract.recognize(imagePath, 'eng', {
            tessedit_char_whitelist: '0123456789'
        });
        const numbers = text.replace(/\D/g, '');
        console.log(`OCR extracted:`, numbers);
        return numbers;
    } catch (err) {
        console.error(`OCR failed:`, err);
        return null;
    }
}

// Create images directory if it doesn't exist
const imagesDir = path.join(__dirname, 'images');
if (!fs.existsSync(imagesDir)) {
    fs.mkdirSync(imagesDir);
    console.log('Created images directory. Please upload your images there.');
}

// Process all images in the images directory
async function processImages() {
    if (fs.existsSync(imagesDir)) {
        const files = fs.readdirSync(imagesDir);
        const imageFiles = files.filter(file => 
            ['.png', '.jpg', '.jpeg', '.gif', '.bmp'].includes(path.extname(file).toLowerCase())
        );
        
        if (imageFiles.length === 0) {
            console.log('No image files found in the images directory. Please upload some images.');
            return;
        }
        
        console.log(`Found ${imageFiles.length} image(s) to process.`);
        
        for (const file of imageFiles) {
            const imagePath = path.join(imagesDir, file);
            console.log(`\nProcessing: ${file}`);
            await scanBarcode(imagePath);
        }
    }
}

// Execute the main function
processImages().catch(err => {
    console.error('Error processing images:', err);
});
