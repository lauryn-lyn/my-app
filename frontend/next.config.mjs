/** @type {import('next').NextConfig} */
const nextConfig = {
  typescript: {
    ignoreBuildErrors: true,
  },
  images: {
    unoptimized: true,
  },
  async rewrites() {
    return {
      beforeFiles: [{ source: '/', destination: '/Swapp-v2.html' }],
    }
  },
}

export default nextConfig
