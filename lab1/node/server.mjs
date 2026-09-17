import { readFileSync } from 'node:fs';
import { createServer } from 'node:http';

const ROUTES = {
  '/': 'index.html',
  '/about': 'about.html',
  '/styles.css': 'styles.css',
};

const server = createServer((req, res) => {
  const path = req.url.split('?')[0];
  const filename = ROUTES[path] ?? '404.html';
  const status = ROUTES[path] ? 200 : 404;

  const filePath = new URL(`./public/${filename}`, import.meta.url);
  const content = readFileSync(filePath, 'utf-8');

  const contentType = filename.endsWith('.css') ? 'text/css; charset=utf-8' : 'text/html; charset=utf-8';

  res.writeHead(status, { 'Content-Type': contentType });
  res.end(content);
});

server.listen(3001, () => console.log('Server running on port 3001'));
