#!/usr/bin/yarn dev

// Import the createClient function from the 'redis' library
import { createClient } from "redis";

// Create a Redis client instance
const client = createClient();

// Event handler for the 'error' event emitted by the Redis client
client.on("error", (err) => {
  // Log an error message when the client encounters an error
  console.log("Redis client not connected to the server:", err.toString());
});

// Event handler for the 'connect' event emitted by the Redis client
client.on("connect", () => {
  // Log a message when the client successfully connects to the server
  console.log("Redis client connected to the server");
});
