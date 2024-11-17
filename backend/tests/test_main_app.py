import pytest
import pytest_asyncio




@pytest.mark.asyncio
async def test_root(client):
    response = client.get('/test')



