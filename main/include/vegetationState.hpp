#ifndef CADMIUM_EXAMPLE_CELLDEVS_VEGETATION_STATE_HPP_
#define CADMIUM_EXAMPLE_CELLDEVS_VEGETATION_STATE_HPP_

#include <iostream>
#include <nlohmann/json.hpp>

//! Vegetation cell state.
struct vegetationState {
	bool vegetation;

	//! Default constructor function.
	vegetationState() : vegetation(false) {}
};

//! prints the state of the vegetation cell in an output stream.
std::ostream& operator<<(std::ostream& os, const vegetationState& x) {
	os << "<" << ((x.vegetation) ? 1 : 0) << ">";
	return os;
}

//! Equality comparison 
bool operator!=(const vegetationState& x, const vegetationState& y) {
	return x.vegetation != y.vegetation;
}

//! JSON config for initial state configuration.
void from_json(const nlohmann::json& j, vegetationState& s) {
	j.at("vegetation").get_to(s.vegetation);
}

#endif 
