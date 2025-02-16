import { ThemeProvider, createTheme } from '@mui/material';
import Dashboard from './components/Dashboard';
import Layout from './Layout';

const theme = createTheme({
  typography: {
    fontFamily: 'Inter, system-ui, Avenir, Helvetica, Arial, sans-serif',
  },
  palette: {
    mode: 'dark',
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Layout>
        <Dashboard />
      </Layout>
    </ThemeProvider>
  );
}

export default App;
