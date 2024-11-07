import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Typography } from '@mui/material';

const RankingTable = ({ rankings, parameters }) => {
  const { startDate, endDate, tierOptions, rankingType, evaluationLevel } = parameters;

  return (
    <Paper elevation={3} className="ranking-table">
      <Typography variant="h6" className="section-title">Player Rankings</Typography>
      <Typography variant="body2" className="parameters">
        Date Range: {startDate} to {endDate} | Tiers: {tierOptions.join(', ')} | 
        Ranking Type: {rankingType} | Evaluation Level: {evaluationLevel}
      </Typography>
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
                <TableCell>{ranking.score}</TableCell>
                <TableCell>{ranking.uncertainty}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Paper>
  );
};

export default RankingTable;
