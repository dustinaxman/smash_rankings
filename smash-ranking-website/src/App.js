import React, { useState, useEffect } from 'react';
import { Container, Grid, Button, Typography } from '@mui/material';
import CircularProgress from '@mui/material/CircularProgress';
import axios from 'axios';
import queryString from 'query-string';
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
  const [loadingRankings, setLoadingRankings] = useState(false);
  const [loadingTournaments, setLoadingTournaments] = useState(false);

  // Load state from URL if present
  useEffect(() => {
    const params = queryString.parse(window.location.search);
    if (params.tierOptions) setTierOptions(params.tierOptions.split(','));
    if (params.startDate) setStartDate(params.startDate);
    if (params.endDate) setEndDate(params.endDate);
    if (params.rankingType) setRankingType(params.rankingType);
    if (params.evaluationLevel) setEvaluationLevel(params.evaluationLevel);
  }, []);

  const fetchTourneySlugs = async () => {
    setLoadingTournaments(true);
    const queryParams = queryString.stringify({
      tier_options: tierOptions.join(','),
      start_date: startDate,
      end_date: endDate,
    });

    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/query_tournaments?${queryParams}`
      );
      setTourneySlugs(response.data.map(item => item.tourney_slug));
    } catch (error) {
      console.error("Error fetching tournaments:", error);
    } finally {
      setLoadingTournaments(false);
    }
  };

  const fetchRankings = async () => {
    setLoadingRankings(true);
    const queryParams = queryString.stringify({
      ranking_to_run: rankingType,
      tier_options: tierOptions.join(','),
      start_date: startDate,
      end_date: endDate,
      evaluation_level: evaluationLevel,
    });

    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/get_ranking?${queryParams}`
      );
      setRankings(response.data);
    } catch (error) {
      console.error("Error fetching rankings:", error);
    } finally {
      setLoadingRankings(false);
    }
  };

  // Handle state updates and update URL
  const handleUpdate = (newState) => {
    setTierOptions(newState.tierOptions);
    setStartDate(newState.startDate);
    setEndDate(newState.endDate);
    setRankingType(newState.rankingType);
    setEvaluationLevel(newState.evaluationLevel);
    const urlParams = queryString.stringify({
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
          {loadingTournaments ? (
            <CircularProgress color="secondary" />
          ) : (
            <TourneyList tourneySlugs={tourneySlugs} />
          )}
        </Grid>
        <Grid item xs={12} md={6}>
          <RankingTable 
            rankings={rankings} 
            parameters={{ startDate, endDate, tierOptions, rankingType, evaluationLevel }} 
            loading={loadingRankings}
          />
        </Grid>
      </Grid>
    </Container>
  );
};

export default App;
