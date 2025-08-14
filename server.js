const express = require("express");
const multer = require("multer");
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");
const os = require("os");
const cors = require("cors");
const rateLimit = require("express-rate-limit");

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static("public"));

const uploadDir = path.resolve("uploads");
if (!fs.existsSync(uploadDir)) fs.mkdirSync(uploadDir, { recursive: true });

const upload = multer({
  storage: multer.diskStorage({
    destination: (req, file, cb) => cb(null, uploadDir),
    filename: (req, file, cb) => {
      const ts = new Date().toISOString().replace(/[:.]/g, "-");
      const name = `${ts}-${crypto.randomBytes(4).toString("hex")}${path.extname(file.originalname) || ".jpg"}`;
      cb(null, name);
    },
  }),
  limits: { fileSize: 5 * 1024 * 1024 },
});

const limiter = rateLimit({ windowMs: 60 * 1000, max: 30 });
app.use(limiter);

function anonymizeIp(ip) {
  const hash = crypto.createHash("sha256").update(ip).digest("hex");
  return hash.slice(0, 16);
}

app.post("/upload", upload.single("photo"), (req, res) => {
  try {
    if (!req.file) return res.status(400).json({ error: "no file" });
    const meta = {
      time: new Date().toISOString(),
      ip_hash: anonymizeIp(req.ip || req.headers["x-forwarded-for"] || "unknown"),
      user_agent: req.headers["user-agent"] || "",
      filename: req.file.filename,
      note: req.body?.note || "",
    };
    fs.appendFileSync(path.join(uploadDir, "log.jsonl"), JSON.stringify(meta) + os.EOL);
    res.json({ ok: true, filename: req.file.filename });
  } catch (e) {
    res.status(500).json({ error: "upload failed" });
  }
});

app.get("/", (req, res) => {
  res.sendFile(path.resolve("public/index.html"));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
