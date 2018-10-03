import logging
import os

from pycoalescence import DispersalSimulation

base_dir = "pycoalescence/pycoalescence/tests"

m = DispersalSimulation(logging_level=logging.CRITICAL)
m.set_simulation_parameters(number_repeats=2, output_database=os.path.join(base_dir, "output/realdispersal9.db"),
							seed=2, sigma=2, landscape_type="closed", number_steps=100)
m.set_map(os.path.join(base_dir, "sample/SA_sample_fine.tif"))
m.add_historical_map(fine_map=os.path.join(base_dir, "sample/SA_sample_fine2.tif"),
					 coarse_map="none", time=10, rate=0.1)
m.run_mean_distance_travelled()
