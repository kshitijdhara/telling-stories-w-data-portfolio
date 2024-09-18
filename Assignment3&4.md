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

Link to Stephen Few's Google Spreadsheet (Google Form responses): [Insert link]

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
I shared my redesign with two different individuals:

### Student (mid-20s):
#### Feedback:
Found the grouped bar chart much easier to interpret than the original stacked chart. However, they found the use of lighter colors confusing.
#### Changes:
Based on this feedback, I adjusted the color intensity for clearer visual differences.

Feedback Summary:
Common Themes: Both participants appreciated the change in chart type but asked for better labeling and clearer colors.
Design Changes: I improved color contrast and added more descriptive labels, making the visualization easier to follow without an explanation.

## Part 5: Final Data Visualization

After gathering feedback, I implemented the following changes:

- Stacked bars instead of Grouped bar chart for more straightforward comparison.
- Improved color scheme with better contrast.
- State labels added to the map for easier identification.
- Hover-over interactivity introduced for additional insights without cluttering the main view.

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
The redesigned data visualization aims to improve clarity, comparability, and engagement. By addressing the weaknesses identified in the critique, the final product allows users to extract more meaningful insights at a glance while providing a more interactive experience. The redesign process taught me how important it is to test visualizations with real users, and I will continue applying these principles in future visualizations.