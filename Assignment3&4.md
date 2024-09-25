---
title: Assignment3&4
layout: template
filename: Assignment3&4.md
---
## Assignment 3 & 4

### Name: Kshitij Dhara
### Andrew ID: kdhara


## Part 1: Original Data Visualization

Link to the Original Visualization: [MakeoverMonday Data Visualization](https://data.world/makeovermonday/generative-ai-search-trends-in-the-united-states)

Why I Selected This Visualization:

I chose this particular data visualization because it represents an important public dataset created by a professional organization/government agency, but I believe its clarity and presentation could be improved for better understanding. The visualization displays key data, but its color choices, layout, and comparison techniques seem to fall short in guiding the audience to gain meaningful insights efficiently.
![Original Visualization](<dataviz img/AI trends OG chart.png>)

## Part2: Critique of the Data Visualization

For the critique, I used Stephen Few's Data Visualization Effectiveness Profile as the primary evaluation tool. Here's a detailed breakdown:

### Clarity

- Data Encoding: The use of color intensity to represent the percentage of searches is clear and effective. It's visually intuitive and easy to interpret.
- Chart Type: The bar chart is a simple and appropriate choice for comparing the interest in different AI tools across regions.
- Labels and Legends: The labels and legends are clear and concise, aiding understanding.

### Accuracy

- Data Accuracy: Assuming the data is accurate, the visualization accurately reflects the search trends.
- Scale: The scale seems appropriate for the data range.

### Relevance

- Message: The visualization effectively communicates the relative interest in Midjourney, Stable Diffusion, and DALL-E across different subregions.
- Audience: The visualization is likely relevant to researchers, developers, and enthusiasts interested in AI art generation.

### Aesthetics

- Visual Appeal: The visualization is visually appealing, with a clean and modern design.
- Color Palette: The color palette is visually distinct and helps differentiate the tools.

### Efficiency

- Ease of Understanding: The visualization is relatively easy to understand, even for those not familiar with data visualization.
- Cognitive Load: The use of color intensity and simple chart type minimizes cognitive load.

Link to Stephen Few's ([Google Form responses](Assignment3&4GoogleForm.pdf))

## Part 3: Redesign Sketches

The focus for the initial redesign ideas was on:

- Changing the chart type: Replacing the geographical map with grouped bar chart or small multiples for better comparison.
- Improving color contrast: Introducing a new color scheme for better differentiation between categories.
- Adding interactivity: Users can click or hover over regions to see detailed breakdowns.

<div class='tableauPlaceholder' id='viz1726693746021' style='position: relative'><noscript><a href='#'><img
                alt='Assignment 3&amp;4 temp '
                src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tw&#47;TwD-Assignment34&#47;Sheet2&#47;1_rss.png'
                style='border: none' /></a></noscript><object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='TwD-Assignment34&#47;Sheet2' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image'
            value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tw&#47;TwD-Assignment34&#47;Sheet2&#47;1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
        <param name='filter' value='publish=yes' />
    </object></div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1726693746021');
    var vizElement = divElement.getElementsByTagName('object')[0];
    vizElement.style.width = '100%';
    vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>


## Part 4: Testing the Redesign

User Feedback:
I shared my redesign with two different individuals and this is what interpreted from their feedback:

### Student (mid-20s):
#### Feedback:
Found the grouped bar chart much easier to interpret than the original stacked chart. However, they found some issues that were confusing:
- The dates are a little confusing for the AI model labels.
- The dual x-axis is causing confusion.
- The visualization is straining on the eyes due to the presence of lots of axes.

### Adult ( mid-40s):
#### Feedback:
Found the grouped bar chart much easier to interpret than the original stacked chart. However, they found some issues that were confusing:
- Grouping related data can help make the chart less straining on the eyes.
- The chart is difficult to interpret visually, considering the distinct, contrasting colors to separate categories more clearly was not as helpful as intended and increased strain on the eyes.

### Changes:
Based on this feedback, what I understood is that both participants appreciated the change in chart type but asked for better labeling and clearer colors which was less strenous on the eyes. I improved color contrast and added more descriptive labels, making the visualization easier to follow without an explanation.

## Part 5: Final Data Visualization

After gathering feedback, I implemented the following changes:

- I replaced the original visualization with a stacked bar chart to allow users to easily compare different regions side by side. This design choice enables users to more quickly identify trends and differences across regions.
- Improved color scheme with better contrast.
- State labels added to the map for easier identification.
- Hover-over interactivity introduced for additional insights without cluttering the main view.
- I restructured the layout so that titles, legends, and key metrics are displayed in a logical, easily readable order. The title is now more prominent, guiding the viewer's attention, while the legend is simplified for quick understanding of color codes.

Final Visualization:
<div class='tableauPlaceholder' id='viz1726693931586' style='position: relative'><noscript><a href='#'><img
                alt='Sheet 1 '
                src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tw&#47;TwD-Assignment34&#47;Sheet1&#47;1_rss.png'
                style='border: none' /></a></noscript><object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='TwD-Assignment34&#47;Sheet1' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image'
            value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tw&#47;TwD-Assignment34&#47;Sheet1&#47;1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
        <param name='filter' value='publish=yes' />
    </object></div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1726693931586');
    var vizElement = divElement.getElementsByTagName('object')[0];
    vizElement.style.width = '100%';
    vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

## Conclusion:
The redesigned data visualization focuses on improving clarity, ease of comparison, and user engagement. By addressing the issues highlighted in the critique, the final version makes it easier for users to quickly grasp key insights while offering an interactive experience to explore the data in more depth. Going through this redesign process taught me how essential it is to test visualizations with real users, as their feedback is invaluable in refining the final product. Moving forward, I’ll continue to prioritize user feedback and ensure my designs are both visually effective and easy to interpret.

## References
- Tableau Software [Tableau Public](https://public.tableau.com)
- [MakeoverMonday](https://makeovermonday.co.uk) - [Generative AI Search Trends in the United States](https://trends.google.com/trends/explore?date=2022-01-01%202024-02-16&geo=US&q=Midjourney,Stable%20Diffusion,DALL%20E&hl=eng)
- [Data.world](https://data.world/makeovermonday/generative-ai-search-trends-in-the-united-states) - [2024/W8 Generative AI Search Trends in the United States](https://data.world/makeovermonday/generative-ai-search-trends-in-the-united-states)
- [Google Trends](https://trends.google.com/trends/explore?date=2022-01-01%202024-02-16&geo=US&q=Midjourney,Stable%20Diffusion,DALL%20E&hl=eng)