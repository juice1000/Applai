import { Typography, Box, Button, Stack, Input } from '@mui/material';
import SendIcon from '@mui/icons-material/Send';
import EditNoteIcon from '@mui/icons-material/EditNote';
import { DataGrid, GridRowParams, GridSearchIcon } from '@mui/x-data-grid';
import { useState, useEffect } from 'react';
import { applyToJobs, fetchJobs, Job, scrapeJobs, writeCoverLetter } from '../libs/api';
import { columns, gridStyles } from './DashboardHelper';
import JobDetailModal from './JobDetailModal';
import ConfirmationModal from './ConfirmationModal';

const Dashboard = () => {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedJobId, setSelectedJobId] = useState<number | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isConfirmationModalOpen, setIsConfirmationModalOpen] = useState(false);

  const loadJobs = async () => {
    try {
      setLoading(true);
      const data = await fetchJobs();
      setJobs(data);
    } catch (error) {
      console.error('Failed to fetch jobs:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleRowDoubleClick = (params: GridRowParams) => {
    setSelectedJobId(params.row.id);
    setIsModalOpen(true);
  };

  const handleApplyToJobs = async () => {
    setLoading(true);
    await applyToJobs();
    loadJobs();
  };

  const handleWriteCoverLetter = async (update?: boolean) => {
    setLoading(true);
    await writeCoverLetter(update);
    loadJobs();
  };

  const handleSearch = async () => {
    if (searchTerm.trim().length === 0) {
      alert('Please enter a search term');
    } else {
      setIsConfirmationModalOpen(true);
    }
  };
  const onSearchConfirm = async () => {
    setLoading(true);
    await scrapeJobs(searchTerm);
    loadJobs();
  };
  // Load jobs on component mount
  useEffect(() => {
    loadJobs();
  }, []);

  let selectedJob: Job | undefined;
  if (selectedJobId) {
    selectedJob = jobs.find((job) => job.id === selectedJobId);
  }

  return (
    <Box sx={{ width: '100%', py: 4, display: 'flex', flexDirection: 'column', gap: 6 }}>
      <Typography
        variant="h2"
        sx={{
          fontWeight: 'bold',
          position: 'relative',
          background: 'linear-gradient(45deg,rgb(1, 129, 233) 0%,rgb(201, 245, 255) 90%)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          backgroundClip: 'text',
          textFillColor: 'transparent',
          '&::before': {
            content: '"Welcome to Applai"',
            position: 'absolute',
            top: 0,
            left: 0,
            background: 'linear-gradient(45deg, rgb(201, 245, 255) 0%, rgb(1, 129, 233) 90%)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text',
            textFillColor: 'transparent',
            opacity: 0,
            transition: 'opacity 2s ease-in-out',
          },
          '&:hover::before': {
            opacity: 1,
          },
        }}
      >
        Welcome to Applai
      </Typography>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Input
          startAdornment={<GridSearchIcon sx={{ cursor: 'pointer' }} onClick={handleSearch} />}
          error={true}
          sx={{
            borderRadius: 100,
            border: 1,
            width: 500,
            '& .MuiSvgIcon-root': {
              position: 'absolute',
              right: '10px',
              top: '50%',
              transform: 'translateY(-50%)',
            },
            '& .Mui-error': {
              borderColor: 'error.main',
              color: 'red',
            },
            paddingX: 2,
          }}
          color="secondary"
          disableUnderline
          placeholder="search new jobs"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter') {
              handleSearch();
            }
          }}
        />
        <Stack direction="row" spacing={2}>
          <Button
            variant="outlined"
            size="large"
            startIcon={<EditNoteIcon />}
            onClick={() => handleWriteCoverLetter(true)}
            sx={{ borderRadius: '50px', fontWeight: 'bold', color: 'lightblue', borderColor: 'lightblue' }}
          >
            Rewrite Cover Letters
          </Button>
          <Button
            variant="outlined"
            size="large"
            startIcon={<EditNoteIcon />}
            onClick={() => handleWriteCoverLetter(false)}
            sx={{ borderRadius: '50px', fontWeight: 'bold', color: 'lightblue', borderColor: 'lightblue' }}
          >
            New Cover Letters
          </Button>
          <Button
            variant="outlined"
            size="large"
            startIcon={<SendIcon />}
            onClick={handleApplyToJobs}
            sx={{ borderRadius: '50px', fontWeight: 'bold', color: 'lightblue', borderColor: 'lightblue' }}
          >
            Bulk Apply
          </Button>
        </Stack>
      </Box>

      {/* Jobs Table Section */}
      <div className="bg-white rounded-lg p-4">
        <Box sx={{ width: '100%', height: '100%' }}>
          <DataGrid
            rows={jobs}
            columns={columns}
            loading={loading}
            slotProps={{
              loadingOverlay: {
                variant: 'skeleton',
                noRowsVariant: 'skeleton',
              },
            }}
            onRowClick={(params) => setSelectedJobId(params.row.id)}
            onRowDoubleClick={handleRowDoubleClick}
            pageSizeOptions={[5, 10]}
            getRowHeight={() => 120}
            sx={gridStyles}
          />
        </Box>
      </div>
      <JobDetailModal open={isModalOpen} onClose={() => setIsModalOpen(false)} job={selectedJob} onUpdate={loadJobs} loading={loading} setLoading={setLoading} />
      <ConfirmationModal searchTerm={searchTerm} open={isConfirmationModalOpen} onClose={() => setIsConfirmationModalOpen(false)} onSearch={onSearchConfirm} />
    </Box>
  );
};

export default Dashboard;
