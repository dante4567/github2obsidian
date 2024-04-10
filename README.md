# github2obsidian
extract basic info from my starred github repos (readme, number of stars, and - most importantly - topics/tags), create markdown for use in obsidian, the github topics/tags are included in obsidian tag-syntax, allowing to facility tag- and link-tools of obsidian (graph-view, tag-extensions....)

## python script github2obsidian.py
### what does the script do?
- Fetches starred repositories from GitHub via API.
- Extracts relevant details about each repository,
  - such as the name,
  - description,
  - topics,
  - README content, and
  - star count.
- Generates a Markdown file for each repository with topics included as obsidian/markdown tags (e.g. topic "mapbox" become #mapbox in the obsidian markdown)


### usage
- download github2obsidian.py
- replace 'YOUR_GITHUB_USERNAME' and 'YOUR_GITHUB_TOKEN' with your data
- set 'OUTPUT_DIR' variable to the dir where you want the Markdown files saved (The script will create this directory if it doesn't exist.
)
- Run the script with Python by navigating to the directory containing your script and using: python github2obsidian.py
- After running the script, you'll find a Markdown file for each starred repository in the specified output directory. These files can then be moved or synced to your Obsidian vault directory for integration into your Zettelkasten.

### next steps
This script serves as a starting point. 
I would love to add more features or refine the existing ones.
It's unlikely to happen ;-) 
If I had the time, energy, expertise, these would be things to consider:
— customize the Markdown formatting
- perform **Tag Clustering** (grouping items based on shared tags to identify similarities or common themes)
- make use of **Topic Modelling**, i.e. going beyound explicit tags, making use of  **Topic Modelling** projects which make use of Latent Dirichlet Allocation (LDA) and the like, to analyze the words in the created markdowns, in order to identify topics that pervade the collection
- try **knowledge graph tools** play with tools like Graphviz or Gephi, pyhton NetworkX, to get a basic understanding how knowledge-graphs are created, appreachiating even more what the obisidan developers have already made look to effortless and easy ;-)
