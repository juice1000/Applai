import { Modal, Box, Typography, IconButton } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import { Job } from '../libs/api';

interface JobDetailModalProps {
  open: boolean;
  onClose: () => void;
  job: Job | null;
}

const modalStyle = {
  position: 'absolute' as const,
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: '80%',
  height: '90%',
  bgcolor: 'background.paper',
  boxShadow: 24,
  p: 4,
  overflow: 'auto',
  borderRadius: '8px',
};

const JobDetailModal = ({ open, onClose, job }: JobDetailModalProps) => {
  if (!job) return null;

  return (
    <Modal open={open} onClose={onClose}>
      <Box sx={modalStyle}>
        <IconButton onClick={onClose} sx={{ position: 'absolute', right: 8, top: 8 }}>
          <CloseIcon />
        </IconButton>

        <Typography variant="h4" component="h2" gutterBottom>
          {job.title}
        </Typography>

        <Box sx={{ mb: 3 }}>
          <Typography variant="subtitle1" color="text.secondary">
            Status: {job.status}
          </Typography>
          <Typography variant="subtitle1" color="text.secondary">
            Date Applied: {job.dateApplied || 'Not applied'}
          </Typography>
        </Box>

        <Typography variant="h6" gutterBottom>
          Keywords
        </Typography>
        <Typography>{job.keywords}</Typography>

        <Typography variant="h6" gutterBottom>
          Description
        </Typography>
        <Typography style={{ whiteSpace: 'pre-wrap' }}>{job.description}</Typography>
      </Box>
    </Modal>
  );
};

export default JobDetailModal;
