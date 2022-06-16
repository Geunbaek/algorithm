const fs = require("fs");
const path = require("path");
const base = path.resolve(__dirname);

const main = () => {
  const args = process.argv.slice(2).reduce((acc, cur) => {
    const [key, val] = cur.split("=");
    return { ...acc, [key]: val };
  }, {});

  if (!("path" in args) || !("file" in args))
    throw new Error(
      `입력 에러 !!\nnode bojTemp.js path=filePath file=fileName 형식으로 작성해주세요.`
    );

  const { path, file } = args;

  fs.exists(`${base}/${path}/${file}.js`, (e) => {
    if (e) {
      throw new Error("이미 존재하는 문제!!");
    }
  });

  const stdin = fs.readFileSync(`${base}/template.js`).toString();
  fs.writeFileSync(`${base}/${path}/${file}.js`, stdin, (err) => {
    if (err) throw err;
  });
};

main();
