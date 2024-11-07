import React from 'react';
import { List, ListItem, ListItemText, Paper, Typography } from '@mui/material';

const TourneyList = ({ tourneySlugs }) => {
  return (
    <Paper elevation={3} className="tourney-list">
      <Typography variant="h6" className="section-title">Tournament Slugs</Typography>
      <List>
        {tourneySlugs.map((slug, index) => (
          <ListItem key={index}>
            <ListItemText primary={slug} />
          </ListItem>
        ))}
      </List>
    </Paper>
  );
};

export default TourneyList;
