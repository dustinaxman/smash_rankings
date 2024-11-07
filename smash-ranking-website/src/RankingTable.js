import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Typography } from '@mui/material';
import CircularProgress from '@mui/material/CircularProgress';

const RankingTable = ({ rankings, parameters, loading }) => {
  const { startDate, endDate, tierOptions, rankingType, evaluationLevel } = parameters;

  return (
    <Paper elevation={3} className="ranking-table">
      <Typography variant="h6" className="section-title">Player Rankings</Typography>
      <Typography variant="body2" className="parameters">
        Date Range: {startDate} to {endDate} | Tiers: {tierOptions.join(', ')} | 
        Ranking Type: {rankingType} | Evaluation Level: {evaluationLevel}
      </Typography>
      {loading ? (
        <div className="loading-container">
          <CircularProgress color="secondary" />
        </div>
      ) : (
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Player</TableCell>
                <TableCell>Mean Rating</TableCell>
                <TableCell>Relative Uncertainty</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {rankings.slice(0, 100).map((ranking, index) => (
                <TableRow key={index}>
                  <TableCell>{ranking.player}</TableCell>
                  <TableCell>{Number(ranking.rating).toFixed(2)}</TableCell>
                  <TableCell>{Number(ranking.uncertainty).toFixed(2)}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Paper>
  );
};

export default RankingTable;
