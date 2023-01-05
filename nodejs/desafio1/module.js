function getFlag(flag) {
  let flagIndex = process.argv.indexOf(flag);
  if (flagIndex >= 3) {
    if (flagIndex < process.argv.length - 1) {
      return process.argv[flagIndex + 1].search(/^--*/) === -1
        ? process.argv[flagIndex + 1]
        : process.argv[flagIndex - 1];
    } else {
      return process.argv[flagIndex - 1];
    }
  }
  return process.argv[flagIndex + 1];
}

module.exports = getFlag;
