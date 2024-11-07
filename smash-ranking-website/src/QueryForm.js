import React from 'react';
import { Grid, TextField, MenuItem, Select, FormControl, InputLabel } from '@mui/material';

const QueryForm = ({ tierOptions, startDate, endDate, rankingType, evaluationLevel, onUpdate }) => {
  const handleChange = (e) => {
    const { name, value } = e.target;
    onUpdate({ ...{ tierOptions, startDate, endDate, rankingType, evaluationLevel }, [name]: value });
  };

  return (
    <Grid container spacing={2} className="query-form">
      <Grid item xs={6} sm={3}>
        <FormControl fullWidth>
          <InputLabel>Tier</InputLabel>
          <Select
            multiple
            name="tierOptions"
            value={tierOptions}
            onChange={handleChange}
          >
            {["P", "S+", "S", "A+", "A", "B+", "B", "C"].map(option => (
              <MenuItem key={option} value={option}>{option}</MenuItem>
            ))}
          </Select>
        </FormControl>
      </Grid>
      <Grid item xs={6} sm={3}>
        <TextField
          label="Start Date"
          type="date"
          name="startDate"
          value={startDate}
          onChange={handleChange}
          fullWidth
        />
      </Grid>
      <Grid item xs={6} sm={3}>
        <TextField
          label="End Date"
          type="date"
          name="endDate"
          value={endDate}
          onChange={handleChange}
          fullWidth
        />
      </Grid>
      <Grid item xs={6} sm={3}>
        <FormControl fullWidth>
          <InputLabel>Ranking Type</InputLabel>
          <Select
            name="rankingType"
            value={rankingType}
            onChange={handleChange}
          >
            <MenuItem value="elo">Elo</MenuItem>
            <MenuItem value="trueskill">TrueSkill</MenuItem>
          </Select>
        </FormControl>
      </Grid>
      <Grid item xs={6} sm={3}>
        <FormControl fullWidth>
          <InputLabel>Evaluation Level</InputLabel>
          <Select
            name="evaluationLevel"
            value={evaluationLevel}
            onChange={handleChange}
          >
            <MenuItem value="sets">Sets</MenuItem>
            <MenuItem value="games">Games</MenuItem>
          </Select>
        </FormControl>
      </Grid>
    </Grid>
  );
};

export default QueryForm;
