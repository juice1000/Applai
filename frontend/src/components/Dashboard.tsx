import { Card, CardContent, Typography, Grid } from '@mui/material';

const dummyData = [
  {
    title: 'Project Management',
    description: 'Streamline your workflow with our intuitive project management tools. Track progress, assign tasks, and meet deadlines effectively.',
  },
  {
    title: 'Data Analytics',
    description: 'Transform raw data into actionable insights. Our powerful analytics dashboard helps you make informed decisions.',
  },
  {
    title: 'Team Collaboration',
    description: 'Foster teamwork and communication with our collaborative features. Share resources and stay connected in real-time.',
  },
  {
    title: 'Resource Planning',
    description: 'Optimize resource allocation and capacity planning. Ensure your team operates at peak efficiency.',
  },
  {
    title: 'Performance Metrics',
    description: 'Monitor key performance indicators and track success metrics. Stay on top of your business goals.',
  },
  {
    title: 'Customer Feedback',
    description: 'Gather and analyze customer feedback to improve your products and services. Build better customer relationships.',
  },
];

const Dashboard = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <Typography variant="h3" className="mb-6 text-gray-800">
        Dashboard
      </Typography>
      <Grid container spacing={4}>
        {dummyData.map((card, index) => (
          <Grid item xs={12} sm={6} md={4} key={index}>
            <Card className="hover:shadow-lg transition-shadow duration-300">
              <CardContent className="min-h-[200px]">
                <Typography variant="h5" component="h2" className="mb-4 text-gray-900">
                  {card.title}
                </Typography>
                <Typography variant="body1" color="text.secondary">
                  {card.description}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </div>
  );
};

export default Dashboard;
