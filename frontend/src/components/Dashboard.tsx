import { Typography, Box } from '@mui/material';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { useState, useEffect } from 'react';
import { fetchJobs, Job } from '../libs/api';

const getStatusColor = (status: string) => {
  switch (status.toLowerCase()) {
    case 'pending':
      return '#fff3e0'; // Light orange
    case 'applied':
      return '#e8f5e9'; // Light green
    case 'rejected':
      return '#ffebee'; // Light red
    default:
      return 'transparent';
  }
};

// Add table data
const columns: GridColDef[] = [
  { field: 'id', headerName: 'ID', width: 70 },
  { field: 'title', headerName: 'Job Title', width: 200 },
  {
    field: 'status',
    headerName: 'Status',
    width: 100,
    renderCell: (params) => (
      <Box
        sx={{
          backgroundColor: getStatusColor(params.value as string),
          padding: '4px 8px',
          borderRadius: '4px',
          width: '100%',
          textAlign: 'center',
        }}
      >
        {params.value}
      </Box>
    ),
  },
  { field: 'keywords', headerName: 'Keywords', width: 200 },
  { field: 'description', headerName: 'Description', width: 200 },
  { field: 'dateApplied', headerName: 'Date Applied', width: 130 },
];

const Dashboard = () => {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadJobs = async () => {
      try {
        const data = await fetchJobs();
        setJobs(data);
      } catch (error) {
        console.error('Failed to fetch jobs:', error);
      } finally {
        setLoading(false);
      }
    };

    loadJobs();
  }, []);

  return (
    <Box sx={{ width: '100%', py: 4 }}>
      <Typography variant="h4">This is a full-width component</Typography>
      <Typography variant="h3" className="mb-6 text-gray-800">
        Dashboard
      </Typography>

      {/* Jobs Table Section */}
      <div className="bg-white rounded-lg p-4">
        <Typography variant="h5" className="mb-4">
          Job Applications
        </Typography>
        <Box sx={{ width: '100%', height: 400 }}>
          <DataGrid
            rows={jobs}
            columns={columns}
            loading={loading}
            initialState={{
              pagination: {
                paginationModel: { page: 0, pageSize: 5 },
              },
            }}
            pageSizeOptions={[5, 10]}
            sx={{
              backgroundColor: 'white',
              '& .MuiDataGrid-root': {
                width: '100%',
              },
              '& .MuiDataGrid-row': {
                '&:hover': {
                  backgroundColor: '#f5f5f5',
                },
              },
            }}
          />
        </Box>
      </div>
    </Box>
  );
};

export default Dashboard;
