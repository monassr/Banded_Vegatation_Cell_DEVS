#ifndef CADMIUM_EXAMPLE_CELLDEVS_VEGETATION_HPP_
#define CADMIUM_EXAMPLE_CELLDEVS_VEGETATION_HPP_

#include <cmath>
#include <nlohmann/json.hpp>
#include <cadmium/modeling/celldevs/grid/cell.hpp>
#include <cadmium/modeling/celldevs/grid/config.hpp>
#include "vegetationState.hpp"

using namespace cadmium::celldevs;

class vegetationCell : public GridCell<vegetationState, double> {
	public:
	vegetationCell(const std::vector<int>& id,
			const std::shared_ptr<const GridCellConfig<vegetationState, double>>& config
		  ): GridCell<vegetationState, double>(id, config) { }

	[[nodiscard]] vegetationState localComputation(vegetationState state,
		const std::unordered_map<std::vector<int>, NeighborData<vegetationState, double>>& neighborhood) const override {

		double rainfall = 0.0;
		double toprow = 0.0;

		for (const auto& [neighborId, neighborData] : neighborhood) {
			double v = neighborData.vicinity;
			if (neighborData.state && neighborData.state->vegetation) {
				if (v > 1.5) {
					// vicinity ~2.0: direct neighbor in both rainfall and toprow
					rainfall += 1.0;
					toprow += 1.0;
				} else if (v > 0.75) {
					 // vicinity ~1.0: direct neighbor in rainfall only
					rainfall += 1.0;
				} else if (v > 0.25) {
					// vicinity ~0.5 : extended neighbor at half weight
					rainfall += 0.5;
				}
				
			}
		}

		if (!state.vegetation) {
			// Case 1: empty cell becomes vegetated if receiving >= 60% rainfall
			if (rainfall >= 5.0) {
				state.vegetation = true;
			}
		} else {
			// Case 2: vegetated cell dies if rainfall + runoff < 9.5
			double totalscore = rainfall + (9.0 - (3.0 * toprow));
			if (totalscore < 9.5) {
				state.vegetation = false;
			}
		}

		return state;
	}

	[[nodiscard]] double outputDelay(const vegetationState& state) const override {
		return 1.0;
	}
};

#endif 
