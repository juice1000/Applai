import { GridColDef } from '@mui/x-data-grid';

export const getStatusColor = (status: string) => {
  switch (status.toLowerCase()) {
    case 'pending':
      return '#ffd54f'; // Vivid yellow
    case 'ready':
      return '#64b5f6'; // Vivid blue
    case 'review':
      return '#b0aac0'; // Vivid purple
    case 'applied':
      return '#81c784'; // Vivid green
    case 'rejected':
      return '#ff8a80'; // Vivid red
    case 'irrelevant':
      return '#b0bec5'; // Vivid grey
    default:
      return 'transparent';
  }
};

// Add table data
export const columns: GridColDef[] = [
  { field: 'id', headerName: 'ID', width: 40, headerClassName: 'super-app-theme--header' },
  {
    field: 'title',
    headerName: 'Job Title',
    width: 200,
    headerClassName: 'super-app-theme--header',
    renderCell: (params) => <div style={{ whiteSpace: 'pre-wrap', lineHeight: '1.2', width: '100%' }}>{params.value}</div>,
  },
  {
    field: 'status',
    headerName: 'Status',
    width: 100,
    headerClassName: 'super-app-theme--header',
    renderCell: (params) => (
      <div
        style={{
          backgroundColor: getStatusColor(params.value as string),
          width: '100%',
          textAlign: 'center',
        }}
      >
        {params.value}
      </div>
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
      backgroundColor: '#f5f5f5',
    },
    '&:hover': {
      backgroundColor: '#e3f2fd !important', // Vivid blue hover
      cursor: 'pointer',
    },
    '&.Mui-selected': {
      backgroundColor: '#e3f2fd !important', // Vivid blue selected
    },
  },
  '& .MuiDataGrid-cell': {
    overflow: 'auto !important',
    whiteSpace: 'normal',
    padding: '8px',
    borderBottom: '1px solid #e0e0e0',
  },
  '& .MuiDataGrid-cell:focus': {
    outline: 'none',
  },
  '& .MuiDataGrid-cell:focus-within': {
    outline: 'none',
  },
  '& .MuiDataGrid-columnHeader:focus': {
    outline: 'none',
  },
  '& .MuiDataGrid-columnHeader:focus-within': {
    outline: 'none',
  },
  '& .MuiDataGrid-columnHeaders': {
    borderBottom: '2px solid #bdbdbd',
  },
  '& .super-app-theme--header': {
    fontWeight: '700',
    fontSize: '1rem',
  },
};
