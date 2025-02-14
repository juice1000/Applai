import React, { ReactNode } from 'react';
import './index.css'; // Make sure to import the CSS file
import { Box } from '@mui/material';

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <Box sx={{ width: '100vw', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Box sx={{ width: '100%', maxWidth: '2000px', margin: '0 auto', px: '3vw' }}>{children}</Box>
    </Box>
  );
};

export default Layout;
