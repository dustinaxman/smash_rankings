import React, { useState, useEffect } from 'react';
import { Container, Grid, Button, Typography } from '@mui/material';
import axios from 'axios';
import { parse, stringify } from 'query-string';
import QueryForm from './QueryForm';
import TourneyList from './TourneyList';
import RankingTable from './RankingTable';
import './App.css';

const App = () => {
  const [tierOptions, setTierOptions] = useState(["P", "S+", "S", "A+", "A"]);
  const [startDate, setStartDate] = useState("2018-11-01");
  const [endDate, setEndDate] = useState(new Date().toISOString().split('T')[0]);
  const [rankingType, setRankingType] = useState("elo");
  const [evaluationLevel, setEvaluationLevel] = useState("sets");
  const [tourneySlugs, setTourneySlugs] = useState([]);
  const [rankings, setRankings] = useState([]);
  
  // Load state from URL if present
  useEffect(() => {
    const params = parse(window.location.search);
    if (params.tierOptions) setTierOptions(params.tierOptions.split(','));
    if (params.startDate) setStartDate(params.startDate);
    if (params.endDate) setEndDate(params.endDate);
    if (params.rankingType) setRankingType(params.rankingType);
    if (params.evaluationLevel) setEvaluationLevel(params.evaluationLevel);
  }, []);

  const fetchTourneySlugs = async () => {
    try {
      const response = await axios.post(
        "https://1234567.execute-api.us-east-1.amazonaws.com/prod/query_tournaments",
        {
          tier_options: tierOptions,
          start_date: startDate,
          end_date: endDate,
        },
        { headers: { "x-api-key": "smash_ranker_api_secret_key" } }
      );
      setTourneySlugs(response.data.map(item => item.tourney_slug));
    } catch (error) {
      console.error("Error fetching tournaments:", error);
    }
  };

  const fetchRankings = async () => {
    try {
      const response = await axios.post(
        "https://1234567.execute-api.us-east-1.amazonaws.com/prod/get_ranking",
        {
          ranking_to_run: rankingType,
          tier_options: tierOptions,
          start_date: startDate,
          end_date: endDate,
          evaluation_level: evaluationLevel,
        },
        { headers: { "x-api-key": "smash_ranker_api_secret_key" } }
      );
      setRankings(response.data);
    } catch (error) {
      console.error("Error fetching rankings:", error);
    }
  };

  // Handle state updates and update URL
  const handleUpdate = (newState) => {
    setTierOptions(newState.tierOptions);
    setStartDate(newState.startDate);
    setEndDate(newState.endDate);
    setRankingType(newState.rankingType);
    setEvaluationLevel(newState.evaluationLevel);
    const urlParams = stringify({
      tierOptions: newState.tierOptions.join(','),
      startDate: newState.startDate,
      endDate: newState.endDate,
      rankingType: newState.rankingType,
      evaluationLevel: newState.evaluationLevel
    });
    window.history.replaceState(null, '', `?${urlParams}`);
    fetchTourneySlugs();
  };

  return (
    <Container maxWidth="lg" className="app-container">
      <Typography variant="h4" className="title">Tournament Ranking Dashboard</Typography>
      <QueryForm 
        tierOptions={tierOptions} startDate={startDate} endDate={endDate}
        rankingType={rankingType} evaluationLevel={evaluationLevel}
        onUpdate={handleUpdate} />
      <Button variant="contained" color="success" onClick={fetchRankings} className="compute-button">
        Compute Ranking
      </Button>
      <Grid container spacing={4} className="content-grid">
        <Grid item xs={12} md={6}>
          <TourneyList tourneySlugs={tourneySlugs} />
        </Grid>
        <Grid item xs={12} md={6}>
          <RankingTable rankings={rankings} parameters={{ startDate, endDate, tierOptions, rankingType, evaluationLevel }} />
        </Grid>
      </Grid>
    </Container>
  );
};

export default App;
