# Data Sources and Maintenance

## How the catalogue is built

The catalogue uses a hybrid collection method. It downloads conference-year JSON lists from [Paper Copilot's `paperlists` repository](https://github.com/papercopilot/paperlists), normalizes their metadata, applies the selection rules below, and links each entry to the paper's public submission or proceedings page when that URL is present in the source record. The `paperlists` project describes itself as a link collection that combines records from sources such as OpenReview, official conference sites, and open-access proceedings. It is a third-party aggregator, not an official conference database.

The configured conference sources are ICLR, ICML, NeurIPS, CVPR, ICCV, ECCV, ACL, EMNLP, NAACL, AAAI, IJCAI, AISTATS, KDD, COLM, CoRL, ICRA, and IROS. Available years differ by conference and by what the upstream source publishes.

For ICLR 2027, the collector reads the public [Paper Copilot rating table](https://papercopilot.com/statistics/iclr-statistics/iclr-2027-statistics/), retrieves the selected paper titles and abstracts from its public listing endpoint, computes mean ratings from the raw posted ratings, and links each paper to its OpenReview forum. Only a short abstract-derived snippet is kept in the generated files; full abstracts are not stored in this repository.

## Selection rules

- For each conference and year, include up to 15 non-rejected papers with at least three public ratings, ordered by mean rating, review count, and reviewer confidence.
- Include records explicitly marked as award recipients.
- Include up to 12 papers marked as oral, spotlight, highlight, or a comparable presentation type.
- If a conference-year has no records selected by those signals, use up to 10 highly cited records when citation data is available.
- The current ICLR 2027 snapshot contains the top 20 submissions with at least three posted ratings. Scores are not compared across conferences because rating scales, reviewer pools, and release stages differ.

Selection is intentionally conservative when a source has no usable score, award, presentation, or citation fields. For example, the available KDD 2024 list contains 562 records but none of those selection signals, so this pipeline currently selects no KDD 2024 papers. That is a source-coverage gap, not a claim that the conference had no notable papers.

## Reliability and limits

Paper Copilot is useful for discovering records and collecting public review snapshots in a consistent format, but its data can be incomplete, delayed, or changed without notice. The repository does not expose an explicit license file for the aggregated dataset. This catalogue therefore stores selected metadata and short descriptions rather than mirroring the raw conference lists, and it keeps links to the underlying paper records. Users should verify consequential bibliographic, award, and review details against the linked OpenReview page or official proceedings.

During the initial link audit, one ACL Anthology URL in the upstream list returned 404 and was excluded; the similarly titled record with a working official proceedings page was retained. This illustrates why the aggregator is treated as a discovery source rather than final authority.

A HEAD check of the remaining 494 unique links returned 200 for 338 and 202 for 20. OpenReview rate-limited 136 requests with HTTP 429, so those links could not be confirmed in this pass. No broken links were inferred from rate-limited responses.

Review ratings are snapshots, not decisions. A public score may change during author response and discussion; some venues release reviews only after decisions or only for papers whose authors opted in. Historical source records do not always preserve when a score was observed relative to rebuttal. Where that phase cannot be established from source data, it is labeled unknown instead of inferred. The current ICLR review phase is derived from the official [ICLR 2027 schedule](https://iclr.cc/Conferences/2027/Dates).

## Can the records be collected directly?

Yes. A fully first-party collector can use OpenReview's public API for submissions and reviews where the venue exposes them, and official proceedings or open-access portals for accepted-paper metadata. Other venues publish proceedings through different systems, including ACL Anthology, CVF Open Access, PMLR, and ACM Digital Library. Each needs its own adapter, field mapping, release-policy handling, and link checks. Review data may be unavailable until a venue releases it, and endpoints can impose rate limits or access restrictions.

During this build, direct unauthenticated requests to both OpenReview API hosts returned HTTP 403 from the current network. This is an access limitation observed in this environment, not evidence that the public API is unavailable to every client. A direct-source collector should check its access from the scheduled GitHub runner before replacing the current feed.

The present pipeline uses the third-party aggregator as a discovery and normalization layer because it already spans many venues. Direct-source adapters are the stronger long-term option for critical fields, particularly review scores and awards. The GitHub workflow isolates source URLs and normalization logic so that venue-specific adapters can be added incrementally. A failed refresh keeps the previous selected records and writes the source error to `data/source_state.json` for inspection.

## Daily update

GitHub Actions runs at 00:17 UTC (08:17 China Standard Time) each day and can also be triggered manually. It checks source ETags, refreshes changed venue-year lists, collects the current ICLR 2027 review snapshot, updates the internal score history, and regenerates `README.md`. GitHub scheduled jobs can start later than their requested time during platform load; the schedule is daily but not a hard real-time guarantee.
