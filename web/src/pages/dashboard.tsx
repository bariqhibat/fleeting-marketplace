import { NextSeo } from 'next-seo';
import Page from '@/components/page';
import Footer from '@/components/footer';
import { useEffect, useState } from 'react';
import axios from 'axios';
import { Button } from 'antd';

export default function Dashboard() {
  const [data, setData] = useState([]);

  return (
    <Page>
      <NextSeo
        title="STARTD - Template"
        description="A TypeScript/Next.js theme that includes everything you need to build amazing landing page!"
      />
      <main>
        <div>Dashboard</div>
        <Button
          onClick={async () => {
            const data = await axios.get('http://localhost:9090/products');

            console.log({ data });
          }}
        >
          Get Data
        </Button>
      </main>
      <Footer />
    </Page>
  );
}
