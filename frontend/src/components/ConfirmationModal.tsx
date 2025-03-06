import { Modal, Box, Typography, Button } from '@mui/material';

interface ConfirmationModalProps {
  open: boolean;
  onClose: () => void;
  searchTerm: string;
  onSearch: () => void;
}

const ConfirmationModal: React.FC<ConfirmationModalProps> = ({ searchTerm, open, onClose, onSearch }) => {
  const handleScrapeJobs = async () => {
    onClose();
    onSearch();
  };

  return (
    <>
      <Modal open={open} onClose={onClose} aria-labelledby="confirmation-modal-title" aria-describedby="confirmation-modal-description">
        <Box
          sx={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            width: 400,
            bgcolor: 'background.paper',
            border: '2px solid #000',
            boxShadow: 24,
            p: 4,
          }}
        >
          <Typography id="confirmation-modal-title" variant="h6" component="h2">
            Confirm Scraping
          </Typography>
          <Typography id="confirmation-modal-description" sx={{ mt: 2 }}>
            Are you sure you want to scrape jobs with the term:
          </Typography>
          <Typography id="confirmation-modal-description" sx={{ mt: 2, fontWeight: 'bold' }}>
            {searchTerm}
          </Typography>
          <Box sx={{ mt: 2, display: 'flex', justifyContent: 'flex-end', gap: 2 }}>
            <Button onClick={onClose} variant="outlined" sx={{ borderRadius: '50px', fontWeight: 'bold', color: 'lightblue', borderColor: 'lightblue' }}>
              Cancel
            </Button>
            <Button variant="contained" onClick={handleScrapeJobs} sx={{ borderRadius: '50px', fontWeight: 'bold', borderColor: 'lightblue' }}>
              Confirm
            </Button>
          </Box>
        </Box>
      </Modal>
    </>
  );
};

export default ConfirmationModal;
