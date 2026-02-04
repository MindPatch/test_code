// Vulnerable Node.js application for testing security scanners
const express = require('express');
const mysql = require('mysql');
const child_process = require('child_process');
const fs = require('fs');
const crypto = require('crypto');

const app = express();

// VULN: Credentials from env (but env vars shown in code)
const DB_PASSWORD = process.env.DB_PASSWORD;
const JWT_SECRET = process.env.JWT_SECRET;
const PRIVATE_KEY = process.env.PRIVATE_KEY;

// VULN: Insecure database connection
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: process.env.DB_PASSWORD,
    database: 'myapp'
});

// VULN: SQL Injection
app.get('/user', (req, res) => {
    const userId = req.query.id;
    const query = "SELECT * FROM users WHERE id = " + userId;
    connection.query(query, (err, results) => {
        res.json(results);
    });
});

// VULN: Command injection
app.get('/exec', (req, res) => {
    const cmd = req.query.cmd;
    child_process.exec(cmd, (err, stdout, stderr) => {
        res.send(stdout);
    });
});

// VULN: Path traversal
app.get('/file', (req, res) => {
    const filename = req.query.name;
    const content = fs.readFileSync('/uploads/' + filename);
    res.send(content);
});

// VULN: XSS - reflected
app.get('/search', (req, res) => {
    const query = req.query.q;
    res.send(`<html><body>Search results for: ${query}</body></html>`);
});

// VULN: Eval injection
app.get('/calc', (req, res) => {
    const expression = req.query.expr;
    const result = eval(expression);
    res.send({ result: result });
});

// VULN: Prototype pollution
app.post('/merge', (req, res) => {
    const target = {};
    const source = req.body;
    for (let key in source) {
        target[key] = source[key];
    }
    res.json(target);
});

// VULN: Weak crypto
function encryptData(data) {
    const cipher = crypto.createCipher('des', 'weak-key');
    return cipher.update(data, 'utf8', 'hex') + cipher.final('hex');
}

// VULN: Insecure random
function generateToken() {
    return Math.random().toString(36).substring(2);
}

// VULN: No rate limiting, listening on all interfaces
app.listen(3000, '0.0.0.0', () => {
    console.log('Server running on port 3000');
});
