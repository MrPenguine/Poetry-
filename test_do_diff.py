import sys
from unittest.mock import MagicMock, patch

# Add the current directory to the path so we can import our modules
sys.path.append('.')

from diff_poetry_lock.run_poetry import do_diff
from diff_poetry_lock.settings import Settings
from diff_poetry_lock.github import GithubApi, GithubComment

# Mock the Settings class
mock_settings = MagicMock(spec=Settings)
mock_settings.event_name = "pull_request"
mock_settings.ref = "refs/pull/123/merge"
mock_settings.repository = "test/repo"
mock_settings.token = "mock_token"
mock_settings.base_ref = "main"
mock_settings.lockfile_path = "poetry.lock"
mock_settings.pr_num.return_value = "123"

# Create a simple test function
def test_do_diff():
    print("Testing do_diff function with mock data...")
    
    # Mock the GithubApi class
    with patch('diff_poetry_lock.run_poetry.GithubApi') as mock_github_api_class:
        # Setup the mock
        mock_api = MagicMock(spec=GithubApi)
        mock_github_api_class.return_value = mock_api
        
        # Mock the load_lockfile function to return empty lists
        with patch('diff_poetry_lock.run_poetry.load_lockfile', side_effect=[[MagicMock()], [MagicMock()]]):
            # Mock list_comments to return an empty list
            mock_api.list_comments.return_value = []
            
            # Call do_diff
            do_diff(mock_settings)
            
            # Verify the function calls
            mock_api.init.assert_called_once_with(mock_settings)
            assert mock_api.post_comment.called or mock_api.update_comment.called or mock_api.delete_comment.called
            
            print("Test completed successfully!")

if __name__ == "__main__":
    test_do_diff()
