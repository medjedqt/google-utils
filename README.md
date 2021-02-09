# google-utils

Use google from the convenience of a python script!

## Installation

Install from pip:

```bash
pip install google-utils
```

## Usage

Fetching links:

```py
from google_utils import Google

results = Google.search("Minecraft")
for result in results:
    print(result.link)
```

Calculator:

```py
from google_utils import Google

response = Google.calculate("64 to the power of six")
print(response.answer)
