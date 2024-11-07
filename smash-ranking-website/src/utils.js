import { parse, stringify } from 'query-string';

export const getInitialStateFromUrl = () => {
  const params = parse(window.location.search);
  return {
    tierOptions: params.tierOptions ? params.tierOptions.split(',') : ["P", "S+", "S", "A+", "A"],
    startDate: params.startDate || "2018-11-01",
    endDate: params.endDate || new Date().toISOString().split('T')[0],
    rankingType: params.rankingType || "elo",
    evaluationLevel: params.evaluationLevel || "sets",
  };
};

export const updateUrl = (state) => {
  const { tierOptions, startDate, endDate, rankingType, evaluationLevel } = state;
  const urlParams = stringify({
    tierOptions: tierOptions.join(','),
    startDate,
    endDate,
    rankingType,
    evaluationLevel
  });
  window.history.replaceState(null, '', `?${urlParams}`);
};
