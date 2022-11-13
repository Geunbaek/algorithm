const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const stdin = fs
  .readFileSync(inputPath)
  .toString()
  .split("\n")
  .map((line) => line.trim());

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const permutations = (array, maxDepth) => {
  const visited = Array(array.length).fill(0);
  const perm = [];

  const recur = (depth, path) => {
    if (depth >= maxDepth) {
      perm.push(path);
      return;
    }

    for (let i = 0; i < array.length; i++) {
      if (visited[i] == 0) {
        visited[i] = 1;
        recur(depth + 1, [...path, i]);
        visited[i] = 0;
      }
    }
  };

  recur(0, []);
  return perm;
};

const deepcopy = (matrix) => JSON.parse(JSON.stringify(matrix));

const rotate = (matrix) => {
  const rotatedMatrix = [];

  for (let x = 0; x < 4; x++) {
    rotatedMatrix.push([]);
    for (let y = 3; y >= 0; y--) {
      rotatedMatrix.at(-1).push(matrix[y][x]);
    }
  }

  return rotatedMatrix;
};

const recur = (depth, kiln, order) => {
  if (depth >= 3) {
    return;
  }

  for (let y = 0; y < 5; y++) {
    for (let x = 0; x < 5; x++) {
      if (!(x >= 0 && x <= 1 && y >= 0 && y <= 1)) {
        continue;
      }
      for (let i = 0; i < 4; i++) {
        const materialInfo = materialDict[order[depth]][i];
        const newKiln = deepcopy(kiln);
      }
    }
  }
};

const putMaterials = (kiln, materials, materialsInfo, sx, sy) => {
  for (let y = sy; y < sy + 4; y++) {
    for (let x = sx; x < sx + 4; x++) {
      const newQuality = kiln[0][y][x] + materials[y - sy][x - sx];
      if (newQuality < 0) {
        kiln[0][y][x] = 0;
      } else if (newQuality > 9) {
        kiln[0][y][x] = 9;
      } else {
        kiln[0][y][x] = newQuality;
      }

      if (materialsInfo[y - sy][x - sx] === "W") {
        continue;
      }
      kiln[1][y][x] = materialsInfo[y - sy][x - sx];
    }
  }
};

const solution = () => {
  const n = Number(input());
  const materialDict = new Map();

  for (let i = 0; i < n; i++) {
    const materials = [];
    const materialsInfo = [];

    for (let j = 0; j < 4; j++) {
      materials.push(input().split(" ").map(Number));
    }

    for (let j = 0; j < 4; j++) {
      materialsInfo.push(input().split(" ").map(Number));
    }

    materialDict[i] = [
      {
        materials,
        materialsInfo,
      },
    ];
    let rotatedMaterials = deepcopy(materials);
    let rotatedMaterialsInfo = deepcopy(materialsInfo);

    for (let j = 0; j < 3; j++) {
      rotatedMaterials = rotate(rotatedMaterials);
      rotatedMaterialsInfo = rotate(rotatedMaterialsInfo);
      materialDict[i].push({
        materials: rotatedMaterials,
        materialsInfo: rotatedMaterialsInfo,
      });
    }
  }

  const materialCase = Array.from({ length: n }, (_, index) => index);
  let answer = 0;
  permutations(materialCase, 3).forEach((perm) => {
    const kiln = Array.from({ length: 2 }, () =>
      Array.from({ length: 5 }, () => Array(5).fill(0))
    );
    // console.log(kiln);
    recur(0, kiln, perm);
  });
};

solution();
