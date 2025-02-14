import { Typography, Box } from '@mui/material';
import { DataGrid, GridRowParams } from '@mui/x-data-grid';
import { useState, useEffect } from 'react';
import { fetchJobs, Job } from '../libs/api';
import { columns, gridStyles } from './DashboardHelper';
import JobDetailModal from './JobDetailModal';

const Dashboard = () => {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedJob, setSelectedJob] = useState<Job | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

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

  const handleRowDoubleClick = (params: GridRowParams) => {
    setSelectedJob(params.row as Job);
    setIsModalOpen(true);
  };

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
        <Box sx={{ width: '100%', height: '100%' }}>
          <DataGrid
            rows={jobs}
            columns={columns}
            loading={loading}
            onRowDoubleClick={handleRowDoubleClick}
            initialState={{
              pagination: {
                paginationModel: { page: 0, pageSize: 30 },
              },
            }}
            pageSizeOptions={[5, 10]}
            getRowHeight={() => 80}
            sx={gridStyles}
          />
        </Box>
      </div>

      <JobDetailModal open={isModalOpen} onClose={() => setIsModalOpen(false)} job={selectedJob} />
    </Box>
  );
};

export default Dashboard;
