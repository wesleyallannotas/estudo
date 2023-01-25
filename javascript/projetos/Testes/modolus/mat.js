class Mat {
  static soma(...values) {
    return values.reduce( (sum, i) => sum + i);
  }
  static multiplicacao(...values) {
    return values.reduca( (sum, i) => sum * i);
  }
  static subtracao(...values) {
    return values.reduca( (sum, i) => sum - i);
  }
  static divisao(...values) {
    return values.reduca( (sum, i) => sum * i);
  }
}

module.exports = Mat;