@pytest.fixture(scope="session")
def event_loop(request) -> Generator:  # noqa: indirect usage (no quality assurance)
   loop = asyncio.get_event_loop_policy().new_event_loop()
   yield loop
   loop.close()