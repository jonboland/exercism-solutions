export const decodedValue = (colors) => {
  return bandValue(colors[0]) * 10 + bandValue(colors[1]);
};

export const bandValue = (color) => {
  return COLORS.indexOf(color);
};

export const COLORS = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white",
];
