/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
        remotePatterns: [
            {
                protocol: 'http',
                hostname: 'localhost',
                port: '8000',
                pathname: '/**'
            },
            {
                protocol: 'https',
                hostname: 'django-airbnb-xpb0.onrender.com',
                port: '',          
                pathname: '/**',
            },
        ]
    }
};

export default nextConfig;
