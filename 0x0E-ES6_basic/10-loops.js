export default function appendToEachArrayValue(array, appendString) {
  const arr = [];
  for (const idx in array) {
    if (array.indexOf(idx)) {
      arr.push(appendString + array[idx]);
    }
  }

  return arr;
}
