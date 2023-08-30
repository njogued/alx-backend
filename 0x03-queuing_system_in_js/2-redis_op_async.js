#!/usr/bin/yarn dev
import { createClient } from "redis";

const client = createClient();

client.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}
function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, val) => {
    if (error) {
      console.log(error);
    } else {
      console.log(val);
    }
  });
}
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
