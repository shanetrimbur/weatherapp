const express = require("express");
const axios = require("axios");
const { BlobServiceClient } = require("@azure/storage-blob");
require("dotenv").config();

const app = express();
const port = process.env.PORT || 3000;

// Azure Blob Storage Config
const connectionString = process.env.AZURE_CONNECTION_STRING;
const containerName = "weathercontainer1";
const blobName = "metar_knkx.json";

// Fetch weather data from Azure Blob
app.get("/weather", async (req, res) => {
  try {
    const blobServiceClient = BlobServiceClient.fromConnectionString(connectionString);
    const containerClient = blobServiceClient.getContainerClient(containerName);
    const blobClient = containerClient.getBlobClient(blobName);
    const downloadBlockBlobResponse = await blobClient.download();
    const data = await streamToBuffer(downloadBlockBlobResponse.readableStreamBody);
    res.json(JSON.parse(data.toString()));
  } catch (err) {
    res.status(500).json({ error: "Failed to fetch weather data" });
  }
});

// Helper function to convert stream to buffer
async function streamToBuffer(readableStream) {
  const chunks = [];
  for await (const chunk of readableStream) {
    chunks.push(chunk);
  }
  return Buffer.concat(chunks);
}

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
