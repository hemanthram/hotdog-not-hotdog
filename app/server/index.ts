import express from "express";
// import multer from "multer";
// import path from "path";
import cors from "cors";
import * as tf from '@tensorflow/tfjs';
// import * as tfn from '@tensorflow/tfjs-node'
// import moment from "moment";

const PORT = process.env.PORT || 8080;

// const storage = multer.memoryStorage();

// const DIR = './images/';
// const storage = multer.diskStorage({
//     destination: (req, file, cb) => {
//         cb(null, DIR);
//     },
//     filename: (req, file, cb) => {
//         cb(null, file.originalname)
//     }
// });

// var upload = multer({
//   storage: storage,
//   fileFilter: (req, file, cb) => {
//     if (
//       file.mimetype == "image/png" ||
//       file.mimetype == "image/jpg" ||
//       file.mimetype == "image/jpeg"
//     ) {
//       cb(null, true);
//     } else {
//       cb(null, false);
//       return cb(new Error("Only .png, .jpg and .jpeg format allowed!"));
//     }
//   },
// });

const app = express();

app.use(express.static(__dirname));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cors());
// app.use("/get", router);

// app.get("/model.json", async (req, res) => {
//   console.log("Done");
//   res.status(200).sendFile(path.join(__dirname, "./jsmodel/model.json"));
// });

app.get("/model", async (req, res) => {
  console.log("Done");
  // const handler = tfn.
  const model = await tf.loadLayersModel("http://localhost:8080/jsmodel/model.json");
  console.log(model.summary())
  if(!!model) res.status(200).send("Done");
  else res.status(200).send("Failed");
});

app.listen(PORT, () => {
  console.log("Server Started");
});