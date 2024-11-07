import React from 'react';
import { Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Typography } from '@mui/material';
import { format } from 'date-fns';

const TourneyList = ({ tourneySlugs }) => {
  return (
    <Paper elevation={3} className="tourney-list">
      <Typography variant="h6" className="section-title">Tournaments</Typography>
      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Tournament ID</TableCell>
              <TableCell>Tier</TableCell>
              <TableCell>Date</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {tourneySlugs.map((tourney, index) => (
              <TableRow key={index}>
                <TableCell>{tourney.tourney_slug}</TableCell>
                <TableCell>{tourney.tier}</TableCell>
                <TableCell>{format(new Date(tourney.date), 'yyyy-MM-dd')}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Paper>
  );
};

export default TourneyList;
