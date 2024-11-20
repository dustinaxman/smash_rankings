import React from 'react';
import { Dialog, DialogTitle, DialogContent, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Button } from '@mui/material';

const DetailSplash = ({ details, onClose }) => {
  const getScore = (score) => {
    // Use parseFloat to convert the score to a number if it's a string
    const numericScore = parseFloat(score);
    // Check if it's a valid number
    return isNaN(numericScore) ? "N/A" : numericScore.toFixed(2);
  };

  return (
    <Dialog open={true} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>Player Win/Loss Details</DialogTitle>
      <DialogContent>
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Type</TableCell>
                <TableCell>Player Name</TableCell>
                <TableCell>Rank</TableCell>
                <TableCell>Count</TableCell>
                <TableCell>Score</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {details.all_wins_and_losses.map((item, index) => (
                <TableRow key={index} style={{ backgroundColor: item.win_count ? "lightgreen" : "lightcoral" }}>
                  <TableCell>{item.win_count ? "WIN" : "LOSS"}</TableCell>
                  <TableCell>{item.player_name}</TableCell>
                  <TableCell>{item.player_rank}</TableCell>
                  <TableCell>{item.win_count || item.loss_count}</TableCell>
                  <TableCell>{getScore(item.score)}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
        <Button onClick={onClose} style={{ marginTop: 16 }} variant="contained" color="secondary">
          Close
        </Button>
      </DialogContent>
    </Dialog>
  );
};

export default DetailSplash;
