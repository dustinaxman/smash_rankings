import React, { useState, useEffect, useRef } from 'react';
import { Container, Grid, Button, Typography } from '@mui/material';
import CircularProgress from '@mui/material/CircularProgress';
import axios from 'axios';
import queryString from 'query-string';
import QueryForm from './QueryForm';
import TourneyList from './TourneyList';
import RankingTable from './RankingTable';
import DetailSplash from './DetailSplash';
import './App.css';

const App = () => {
  const currentRequestId = useRef(0);
  const [tierOptions, setTierOptions] = useState(["P", "S+", "S", "A+", "A"]);
  const [startDate, setStartDate] = useState("2018-11-01");
  const [endDate, setEndDate] = useState(new Date().toISOString().split('T')[0]);
  const [rankingType, setRankingType] = useState("elo");
  const [evaluationLevel, setEvaluationLevel] = useState("sets");
  const [tourneySlugs, setTourneySlugs] = useState([]);
  const [rankings, setRankings] = useState([]);
  const [loadingRankings, setLoadingRankings] = useState(false);
  const [loadingTournaments, setLoadingTournaments] = useState(false);
  const [initializedFromUrl, setInitializedFromUrl] = useState(false);

  const [selectedDetails, setSelectedDetails] = useState(null); // For splash details
  const [lastUsedParameters, setLastUsedParameters] = useState({
    startDate,
    endDate,
    tierOptions,
    rankingType,
    evaluationLevel
  });

  const fetchTourneySlugs = async () => {
    setLoadingTournaments(true);
    const queryParams = queryString.stringify({
      tier_options: tierOptions.join(','),
      start_date: startDate,
      end_date: endDate,
    });

    try {
      const response = await axios.get(
        `https://wn46de3eo7.execute-api.us-east-1.amazonaws.com/prod/query_tournaments?${queryParams}`
      );
      setTourneySlugs(response.data);
    } catch (error) {
      console.error("Error fetching tournaments:", error);
    } finally {
      setLoadingTournaments(false);
    }
  };

  const fetchRankings = async () => {
    const requestId = currentRequestId.current + 1;
    currentRequestId.current = requestId;
    setLoadingRankings(true);

    // Ensure "elo_normalized_by_uncertainty" is treated as "elo" for the API request
    const queryParams = queryString.stringify({
      ranking_to_run: rankingType === "elo_normalized_by_uncertainty" ? "elo" : rankingType,
      tier_options: tierOptions.join(','),
      start_date: startDate,
      end_date: endDate,
      evaluation_level: evaluationLevel,
    });
//http://127.0.0.1:8000
    try {
      const response = await axios.get(
        `https://wn46de3eo7.execute-api.us-east-1.amazonaws.com/prod/get_ranking?${queryParams}`
      );
      console.log(response);
      if (requestId === currentRequestId.current) {
        setRankings(response.data);
      }
    } catch (error) {
      console.error("Error fetching rankings:", error);
    } finally {
      if (requestId === currentRequestId.current) {
        setLoadingRankings(false);
      }
    }
};

  useEffect(() => {
    const params = queryString.parse(window.location.search);
    let shouldFetchRankings = false;

    if (params.tierOptions) {
      setTierOptions(params.tierOptions.split(','));
      shouldFetchRankings = true;
    }
    if (params.startDate) {
      setStartDate(params.startDate);
      shouldFetchRankings = true;
    }
    if (params.endDate) {
      setEndDate(params.endDate);
      shouldFetchRankings = true;
    }
    if (params.rankingType) {
      setRankingType(params.rankingType);
      shouldFetchRankings = true;
    }
    if (params.evaluationLevel) {
      setEvaluationLevel(params.evaluationLevel);
      shouldFetchRankings = true;
    }

    setInitializedFromUrl(shouldFetchRankings);

    if (shouldFetchRankings) {
      fetchRankings();
    }
  }, []);

  useEffect(() => {
    fetchTourneySlugs();
  }, [tierOptions, startDate, endDate]);

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

  const handleComputeRanking = () => {
    // Update lastUsedParameters immediately on button press
    setLastUsedParameters({
      startDate,
      endDate,
      tierOptions,
      rankingType,
      evaluationLevel
    });
    // Call fetchRankings to get the latest rankings data
    fetchRankings();
  };

  const handleRowClick = (details) => {
    setSelectedDetails(details);
  };

  const closeSplash = () => {
    setSelectedDetails(null);
  };

  return (
    <Container maxWidth="lg" className="app-container">
      <Typography variant="h4" className="title">Tournament Ranking Dashboard</Typography>
      <QueryForm 
        tierOptions={tierOptions} startDate={startDate} endDate={endDate}
        rankingType={rankingType} evaluationLevel={evaluationLevel}
        onUpdate={handleUpdate} />
      <Button variant="contained" color="success" onClick={handleComputeRanking} className="compute-button">
        Compute Ranking
      </Button>
      <div className="content-flex-container">
        <div style={{ flex: 1 }}>
          {loadingTournaments ? (
            <CircularProgress color="secondary" />
          ) : (
            <TourneyList tourneySlugs={tourneySlugs} />
          )}
        </div>
        <div style={{ flex: 1 }}>
          <RankingTable 
            rankings={rankings} 
            parameters={lastUsedParameters}
            loading={loadingRankings}
            onRowClick={handleRowClick}
          />
        </div>
      </div>
      {selectedDetails && (
        <DetailSplash 
          details={selectedDetails} 
          onClose={closeSplash} 
        />
      )}
    </Container>
  );
};

export default App;
