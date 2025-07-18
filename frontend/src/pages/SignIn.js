import * as React from 'react';
import axios from 'axios';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import Divider from '@mui/material/Divider';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import MuiCard from '@mui/material/Card';
import { styled } from '@mui/material/styles';
import AppTheme from '../theme/AppTheme';
import ColorModeSelect from '../theme/ColorModeSelect';

const Card = styled(MuiCard)(({ theme }) => ({
  display: 'flex',
  flexDirection: 'column',
  alignSelf: 'center',
  width: '100%',
  padding: theme.spacing(4),
  gap: theme.spacing(2),
  margin: 'auto',
  [theme.breakpoints.up('sm')]: {
    maxWidth: '600px',
  },
  maxHeight: '100dvh',
  overflowY: 'auto',
  boxShadow:
    'hsla(220, 30%, 5%, 0.05) 0px 5px 15px 0px, hsla(220, 25%, 10%, 0.05) 0px 15px 35px -5px',
}));

const SignInContainer = styled(Stack)(({ theme }) => ({
  height: 'calc((1 - var(--template-frame-height, 0)) * 100dvh)',
  minHeight: '100%',
  padding: theme.spacing(2),
  [theme.breakpoints.up('sm')]: {
    padding: theme.spacing(4),
  },
  '&::before': {
    content: '""',
    display: 'block',
    position: 'absolute',
    zIndex: -1,
    inset: 0,
    backgroundImage:
      'radial-gradient(ellipse at 50% 50%, hsl(210, 100%, 97%), hsl(0, 0%, 100%))',
    backgroundRepeat: 'no-repeat',
    ...theme.applyStyles('dark', {
      backgroundImage:
        'radial-gradient(at 50% 50%, hsla(210, 100%, 16%, 0.5), hsl(220, 30%, 5%))',
    }),
  },
}));

export default function SignIn(props) {
  const [password, setPassword] = React.useState('');
  const [loading, setLoading] = React.useState(false);

  const [strength, setStrength] = React.useState('');
  const [hibp, setHibp] = React.useState('');
  const [llmAdvice, setLlmAdvice] = React.useState('');
  const [error, setError] = React.useState('');

  const handleCheckPassword = async () => {
    if (!password) return;

    setLoading(true);
    setStrength('');
    setHibp('');
    setLlmAdvice('');
    setError('');

    try {
      const res = await axios.post('http://localhost:5000/api/predict_password', {
        password: password,
      });

      const { strength, hibp, llm_advice } = res.data;
      setStrength(strength);
      setHibp(hibp);
      setLlmAdvice(llm_advice);
    } catch (err) {
      console.error(err);
      setError('Greška pri komunikaciji sa serverom.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <AppTheme {...props}>
      <CssBaseline enableColorScheme />
      <SignInContainer direction="column" justifyContent="center">
        <ColorModeSelect sx={{ position: 'fixed', top: '1rem', right: '1rem' }} />

        <Card variant="outlined">
          <Typography variant="h6" fontWeight={600}>
            Password Security Check
          </Typography>

          <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
            Enter your password to check its strength, see if it’s been breached, and get AI-powered advice.
          </Typography>

          <TextField
            label="Enter password"
            name="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            size="small"
            margin="dense"
            fullWidth
          />

          <Button
            variant="contained"
            color="primary"
            onClick={handleCheckPassword}
            disabled={loading}
          >
            {loading ? 'Checking...' : 'Check Password'}
          </Button>

          <Divider sx={{ my: 2 }} />

          {error && (
            <Typography color="error" sx={{ mt: 1 }}>
              {error}
            </Typography>
          )}

          {strength && (
            <Box sx={{ mt: 2 }}>
              <Typography variant="subtitle1" fontWeight={600}>Strength(0-2):</Typography>
              <Typography color="text.secondary">{strength}</Typography>
            </Box>
          )}

          {hibp && (
            <Box sx={{ mt: 2 }}>
              <Typography variant="subtitle1" fontWeight={600}>
                Breach Check:
              </Typography>
              <Typography color={hibp.pwned ? 'error' : 'text.secondary'}>
                {hibp.message}
              </Typography>
            </Box>
          )}


          {llmAdvice && (
            <Box sx={{ mt: 2 }}>
              <Typography variant="subtitle1" fontWeight={600}>AI Advice:</Typography>
              <Typography color="text.secondary">{llmAdvice}</Typography>
            </Box>
          )}
        </Card>
      </SignInContainer>
    </AppTheme>
  );
}
