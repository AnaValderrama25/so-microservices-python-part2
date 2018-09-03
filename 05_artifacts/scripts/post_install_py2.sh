#!/bin/bash
# echo "export GM_ANALYTICS=%{python2_sitelib}/gm_analytics/swagger/indexer.yaml >> ~/.bashrc
echo "export GM_ANALYTICS=/usr/lib/python2.7/site-packages/gm_analytics/swagger/indexer.yaml" >> ~/.bashrc
pip install -r requirements.txt
connexion run $GM_ANALYTICS --verbose -p 8088 &
