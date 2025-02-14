import { Box } from '@mui/material';
import { GridColDef } from '@mui/x-data-grid';

export const getStatusColor = (status: string) => {
  switch (status.toLowerCase()) {
    case 'pending':
      return '#fff3e0'; // Light orange
    case 'applied':
      return '#e8f5e9'; // Light green
    case 'rejected':
      return '#ffebee'; // Light red
    case 'irrelevant':
      return '#ffebee'; // Light red
    default:
      return 'transparent';
  }
};

// Add table data
export const columns: GridColDef[] = [
  { field: 'id', headerName: 'ID', width: 40, headerClassName: 'super-app-theme--header' },
  { field: 'title', headerName: 'Job Title', width: 200, headerClassName: 'super-app-theme--header' },
  {
    field: 'status',
    headerName: 'Status',
    width: 100,
    headerClassName: 'super-app-theme--header',
    renderCell: (params) => (
      <Box
        sx={{
          backgroundColor: getStatusColor(params.value as string),
          borderRadius: '4px',
          width: '100%',
          margin: 0,
          textAlign: 'center',
        }}
      >
        {params.value}
      </Box>
    ),
  },
  {
    field: 'keywords',
    headerName: 'Keywords',
    flex: 1,
    minWidth: 200,
    headerClassName: 'super-app-theme--header',
    renderCell: (params) => <div style={{ whiteSpace: 'pre-wrap', lineHeight: '1.2', width: '100%' }}>{params.value}</div>,
  },
  {
    field: 'description',
    headerName: 'Description',
    flex: 2,
    minWidth: 300,
    headerClassName: 'super-app-theme--header',
    renderCell: (params) => <div style={{ whiteSpace: 'pre-wrap', lineHeight: '1.2', width: '100%' }}>{params.value}</div>,
  },
  { field: 'dateApplied', headerName: 'Date Applied', width: 120, headerClassName: 'super-app-theme--header' },
];

export const gridStyles = {
  backgroundColor: 'white',
  '& .MuiDataGrid-root': {
    width: '100%',
  },
  '& .MuiDataGrid-row': {
    '&:nth-of-type(even)': {
      backgroundColor: '#e6e6e6',
    },
    '&:hover': {
      backgroundColor: '#c4c4c4 !important',
      cursor: 'pointer',
    },
  },
  '& .MuiDataGrid-cell': {
    overflow: 'auto !important',
    whiteSpace: 'normal',
    padding: '8px',
    borderBottom: '1px solid #e0e0e0',
  },
  '& .MuiDataGrid-columnHeaders': {
    borderBottom: '2px solid #bdbdbd',
  },
  '& .super-app-theme--header': {
    fontWeight: '700',
    fontSize: '1rem',
  },
};
