const GIGASECOND_IN_MS = 10 ** 12;

export const gigasecond = (moment) => {
  return new Date(moment.getTime() + GIGASECOND_IN_MS);
};
