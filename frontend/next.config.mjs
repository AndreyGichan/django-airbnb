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
                hostname: 'django-airbnb.onrender.com',
                pathname: '/media/**',
            },,
            {
                protocol: 'https',
                hostname: 'rzjfusywfooxdatlzbgj.supabase.co',
                pathname: '/storage/v1/object/public/images/**',
            },
        ]
    }
};

export default nextConfig;
