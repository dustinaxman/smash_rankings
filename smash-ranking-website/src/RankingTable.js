import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Typography } from '@mui/material';
import CircularProgress from '@mui/material/CircularProgress';

const RankingTable = ({ rankings, parameters, loading, onRowClick }) => {
  const { startDate, endDate, tierOptions, rankingType, evaluationLevel } = parameters;

  const transformRating = (rating, uncertainty) => {
    if (uncertainty > 70) {
      return "Honorable Mention";
    }
    return rating * ((1 / (1 + Math.exp((uncertainty - 21) / 200))) + 0.5);
  };

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
              {rankings.slice(0, 100).map((ranking, index) => {
                const ratingToDisplay =
                  rankingType === "elo_normalized_by_uncertainty"
                    ? transformRating(Number(ranking.rating), Number(ranking.uncertainty))
                    : Number(ranking.rating);

                return (
                  <TableRow
                    key={index}
                    onClick={() => {
                      if (ranking.player_win_loss_interpretation) {
                        onRowClick(ranking.player_win_loss_interpretation);
                      }
                    }}
                    style={{
                      cursor: ranking.player_win_loss_interpretation ? "pointer" : "default",
                      backgroundColor: ranking.player_win_loss_interpretation ? "#f9f9f9" : "inherit",
                    }}
                    className={ranking.player_win_loss_interpretation ? "clickable-row" : ""}
                  >
                    <TableCell>{ranking.player}</TableCell>
                    <TableCell>
                      {typeof ratingToDisplay === 'number' 
                        ? ratingToDisplay.toFixed(2) 
                        : ratingToDisplay}
                    </TableCell>
                    <TableCell>{Number(ranking.uncertainty).toFixed(2)}</TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Paper>
  );
};

export default RankingTable;
